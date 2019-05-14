
# Create your tests here.
import requests, json
import unittest

# Create your tests here.


class ShipTraderAPI(unittest.TestCase):

    def test_starships_api(self):
        resp = requests.get('http://0.0.0.0:8008/api/starships/')
        print (resp.status_code)
        self.assertEqual(resp.status_code, 200)

    def test_create_new_ship_listing(self):
        headers = {
                    'Content-Type': 'application/json; charset=utf-8'
                  }
        data = {"name":"Sentinel-class landing craft", "price":390, "active":True, "ship_type":2 }
        resp = requests.post('http://0.0.0.0:8008/api/listing/',data=json.dumps(data), headers=headers)
        print(resp.status_code, resp.text)

    def test_lising_api(self):
        resp = requests.get('http://0.0.0.0:8008/api/starships/1')
        print (resp.status_code)
        print (json.loads(resp.text))
        self.assertEqual(resp.status_code, 200)



    if __name__ == '__main__':
        unittest.main()