import API_calls
import user

temp = API_calls.APIStock()

print([i[0] for i in temp.stockList])