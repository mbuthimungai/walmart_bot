from tools.tool import TryExcept, Response, yaml_load, userAgents, domain 
from parsel import Selector
import json
import time


class Walmart:
    """
    The Walmart class provides methods for scraping data from walmart.com.

    Attributes:
        headers (dict): A dictionary containing the user agent to be used in the request headers.
        catch (TryExcept): An instance of TryExcept class, used for catchig exceptions.
        scrape (yaml_load): An instance of the yaml_load class, used for selecting page elements to be scraped.
    """
    def __init__(self, userInput) -> None:
        """
        Initializes an instance of the Walmart class.
        """
        self.userInput = userInput
        self.country_domain = domain(userInput)
        self.headers = {"User-Agent": userAgents()}
        self.catch = TryExcept()
        self.scrape = yaml_load('selector')
        
    async def status(self):
        response = await Response(self.base_url).response()
        return response
    
    async def product_data_by_search(self):
        content = await Response(self.userInput).content()        
        sel = Selector(text=content)
        # with open("file.txt", "w", encoding="utf-8") as file:
        #     file.write(str(content))
        data = sel.xpath('//script[@id="__NEXT_DATA__"]/text()').get()
        data = json.loads(data)
        products_data = data["props"]["pageProps"]["initialData"]["searchResult"]["itemStacks"][0]["items"]
        
        formatted_product_data = []
        
        for product_data in products_data:
            formatted_product = {
                "current_price": product_data.get("price"),
                "availability": product_data.get("availabilityStatusDisplayValue"),
                "item_id": product_data.get("usItemId"),
                "canonical_url": product_data.get("canonicalUrl"),
                "average_rating": product_data.get("rating", {}).get("averageRating"),
                "image_link": product_data.get("imageInfo", {}).get("thumbnailUrl"),
                "product_name": product_data.get("name"),
                "review_count": product_data.get("rating", {}).get("numberOfReviews")
            }
            
            # Check if all values in the dictionary are None
            if not all(value is None for value in formatted_product.values()):
                formatted_product_data.append(formatted_product)

        # 'formatted_product_data' now contains the formatted product information
        
        return formatted_product_data        

    async def getDepartmentsLinks(self):
        content = await Response(self.userInput).content()                        
        sel = Selector(text=content)        
        data = sel.xpath('//script[@id="__NEXT_DATA__"]/text()').get()        
        data = json.loads(data)
        # categories_data = data["props"]["pageProps"]["initialData"]["contentLayout"]["modules"][0]["configs"]["categories"]
        electronics_data_sub = data["props"]["pageProps"]["initialData"]["contentLayout"]["modules"][0]["configs"]["categories"][3]["subcategories"]
        for electronic_data_sub in electronics_data_sub[1:]:
            subcategory_link = electronic_data_sub["subCategoryLink"]["clickThrough"]["value"]
            if not subcategory_link.startswith("http"):
                subcategory_link = f'https://www.walmart.com{subcategory_link}'            
            print(subcategory_link)
    
    async def product_data_by_category(self):  
        content = await Response(self.userInput).content()
        resp_status_code = await Response(self.userInput).response()
        sel = Selector(text=content)
        data = sel.xpath('//script[@id="__NEXT_DATA__"]/text()').get() 
        return [data, resp_status_code]
        
    async def extract_product_details(self, products_data: list):
        formatted_product_data = []
        
        for product_data in products_data:
            formatted_product = {
                "current_price": product_data.get("price"),
                "availability": product_data.get("availabilityStatusDisplayValue"),
                "item_id": product_data.get("usItemId"),
                "canonical_url": product_data.get("canonicalUrl"),
                "average_rating": product_data.get("rating", {}).get("averageRating"),
                "image_link": product_data.get("imageInfo", {}).get("thumbnailUrl"),
                "product_name": product_data.get("name"),
                "review_count": product_data.get("rating", {}).get("numberOfReviews")
            }
            # print(formatted_product)
            # print("\n")
            # Check if all values in the dictionary are None
            if not all(value is None for value in formatted_product.values()):
                formatted_product_data.append(formatted_product)
            print("Extracted....")
        # 'formatted_product_data' now contains the formatted product information
        return formatted_product_data        
        