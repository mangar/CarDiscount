from pydantic import BaseModel


class MyBaseModel(BaseModel):

    def __repr__(self):
        fields = ", ".join(f"{k}={repr(v)}" for k, v in self.__dict__.items())
        return f"{self.__class__.__name__}({fields})"