import time
from hashlib import md5
from concurrent.futures import ProcessPoolExecutor, wait
from typing import List, Iterator
import zerorpc
from logger import log
HOST = "0.0.0.0"
PORT = 5000
WORKER = 4


def _md5_func(text: str) -> str:
    """md5哈希."""
    start = time.time()
    result = md5(text.encode("utf-8")).hexdigest()
    end = time.time()
    log.info("time it", seconds=end - start)
    return result


def main():
    with ProcessPoolExecutor(WORKER) as executor:
        class HelloRPC:

            def _stream_md5(self, texts: List[str]) -> Iterator[str]:
                for text in texts:
                    fut = executor.submit(_md5_func, text)
                    wait([fut])
                    yield fut.result()

            @zerorpc.stream
            def streaming_md5(self, texts: List[str]) -> Iterator[str]:
                return self._stream_md5(texts)

        s = zerorpc.Server(HelloRPC())
        s.bind(f"tcp://{HOST}:{PORT}")
        s.run()


if __name__ == "__main__":
    main()
