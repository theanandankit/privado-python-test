import functools
import requests
import retrying

class RetriableSession(requests.Session):
    def __init__(
        self,
        stop_max_attempt_number=5,
        wait_fixed=1000 * 60,
        retry_status=(500),
        retry_kwargs=None,
    ):
        super(RetriableSession, self).__init__()

        # Check response status against configuration
        def should_retry_on_response(response: requests.Response) -> bool:
            for error_family in (500, 400, 300, 200):
                # will return 500 for 503 or 400 for 404
                if (response.status_code // error_family) * error_family in retry_status:
                    return True

            if response.status_code in retry_status:
                return True

            return False

        kwargs = {
            'stop_max_attempt_number': stop_max_attempt_number,
            'wait_fixed': wait_fixed,
            'retry_on_result': should_retry_on_response if retry_status else None,
        }
        kwargs.update(retry_kwargs or {})

        def unwrap_retry_error(f):
            @functools.wraps(f)
            def wrapper(*args, **kwargs):
                try:
                    return f(*args, **kwargs)
                except retrying.RetryError as e:
                    if isinstance(e.last_attempt.value, requests.Response):
                        e.last_attempt.value.raise_for_status()
                    else:
                        raise

            return wrapper
        
        self.get = unwrap_retry_error(retrying.retry(**kwargs)(self.get))
        self.post = unwrap_retry_error(retrying.retry(**kwargs)(self.post))
        self.put = unwrap_retry_error(retrying.retry(**kwargs)(self.put))
        self.delete = unwrap_retry_error(retrying.retry(**kwargs)(self.delete))
        self.patch = unwrap_retry_error(retrying.retry(**kwargs)(self.patch))