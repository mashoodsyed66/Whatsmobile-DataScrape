import scrapy


class MobspiderSpider(scrapy.Spider):
    name = "mobspider"
    allowed_domains = ["whatmobile.com.pk"]
    start_urls = ["https://whatmobile.com.pk"]
    i = 0

    def parse(self, response):
        sec = response.css('section')
        sec= sec[1:7]
        visited_urls = [] 
        
        for section in sec:
            relative_url = section.css('h2.hdng a').attrib['href']
            mobs_url = "https://whatmobile.com.pk" + relative_url
            visited_urls.append(mobs_url)
            yield response.follow(url=mobs_url, callback=self.parse2)
        print("Visited URLs:", visited_urls)

    def parse2(self, response):
        table=response.css('table')
        i = self.i + 1  # Use self.i instead of i to keep track of the iteration count
        self.i = i
        print('****************************************************************')
        print("Iteration:", i)
        print("Total tables found:", len(table)
              )
        try:
            table = table[16]
        except IndexError:
            print("Error occurred for URL:", response.url)
            return  # Skip processing further if an error occurs
        
        table_rows = table.css('table tr:has(td.BiggerText)')
        
        for row in table_rows:
        # Extracting all the relative URLs of mobile phones in the row
            relative_urls = row.css('td.BiggerText a::attr(href)').getall()
            for relative_url in relative_urls:
                absolute_url = response.urljoin(relative_url)
                yield scrapy.Request(absolute_url, callback=self.parse_mobile)

    # spider file

    def parse_mobile(self, response):
        name = response.css('h1::text').get()
        specs = response.css('table')[0]
        specs2 = response.css('table')[1]

        os = specs.css("th:contains('OS') + td::text").get()
        weight = specs.css("th:contains('Weight') + td::text").get()
        if weight:
            print(weight)
        else:
            print('NO')
        print(os)
        sim = specs.css("th:contains('SIM') + td::text").get()
        band_4g = specs.css("th:contains('4G Band') + td::text").get()
        cpu = specs.css("th:contains('CPU') + td::text").get()
        chipset = specs.css("th:contains('Chipset') + td::text").get()
        gpu = specs.css("th:contains('GPU') + td::text").get()
        display_tech = specs.css("th:contains('Technology') + td::text").get()
        display_size = specs.css("th:contains('Size') + td::text").get()
        display_resolution = specs.css("th:contains('Resolution') + td::text").get()
        display_extra_features = specs.css("th:contains('Extra Features') + td::text").get()
        memory_built_in = specs.css("th:contains('Built-in') + td::text").get()
        card = specs.css("th:contains('Card') + td::text").get()
        camera_main = specs.css("th:contains('Main') + td::text").get()
        camera_features = specs.css("th:contains('Features') + td::text").get()
        camera_front = specs.css("th:contains('Front') + td::text").get()
        wlan = specs.css("th:contains('WLAN') + td::text").get()
        gps = specs.css("th:contains('GPS') + td::text").get()
        data = specs.css("th:contains('Data') + td::text").get()
        sensors = specs.css("th:contains('Sensors') + td::text").get()
        extra_features = specs.css("th:contains('Extra') + td::text").get()
        battery_capacity = specs.css("th:contains('Capacity') + td::text").get()
        price = specs2.css("tr.RowBG2 th:contains('Price') + td strong::text").get()
        rating = specs2.css("tr.RowBG2 th:contains('Ratings') + td strong::text").get()

        data = {
            "Name": name,
            "OS": os,
            "Weight": weight,
            "SIM": sim,
            "4G Band": band_4g,
            "CPU": cpu,
            "Chipset": chipset,
            "GPU": gpu,
            "Display Technology": display_tech,
            "Display Size": display_size,
            "Display Resolution": display_resolution,
            "Display Extra Features": display_extra_features,
            "Memory Built-in": memory_built_in,
            "Card": card,
            "Camera Main": camera_main,
            "Camera Features": camera_features,
            "Camera Front": camera_front,
            "WLAN": wlan,
            "GPS": gps,
            "Data": data,
            "Sensors": sensors,
            "Extra Features": extra_features,
            "Battery Capacity": battery_capacity,
            "Price": price,
            "Rating": rating
        }

        yield data


