from app.models.product_field_type import ProductFieldType

HTTP_REQUEST_RETRY_CNT = 5
HTTP_REQUEST_RETRY_DELAY = 10
TOKEN = "auth-token"
DENTALSTALL_SCRAP_FIELDS = [ProductFieldType.TITLE.name, ProductFieldType.PRICE.name, ProductFieldType.IMAGE_PATH.name]