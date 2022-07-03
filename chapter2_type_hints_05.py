from optparse import Option
from typing import Optional

def greeting(name: Optional[str] = None):
  return f"Hello, {name if name else 'Anonymous'}"