from pydantic import BaseModel

class Comment(BaseModel):
    id: int
    id_product: int
    content: str
    # class Config:
    #     orm_mode = True  # Để ánh xạ 


class Comment(BaseModel):
    id_product: int
    TGDD_link: str
    FPT_link: str 
    Cellphone_link: str   

class Comment_predict():
    id_comment: int
    category: str
    polarity: str

class list_Comment_predict():
    id_product: int
    category: str
    polarity: str

class TextRequest(BaseModel):
    text: str

