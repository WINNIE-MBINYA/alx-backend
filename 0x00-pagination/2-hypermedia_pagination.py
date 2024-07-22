#!/usr/bin/env python3
"""
Main file
"""

from math import ceil  # Import for ceiling function

Server = __import__('2-hypermedia_pagination').Server


class Server:
    """
    Server class for hypermedia pagination
    """

    def __init__(self):
        self.data = [  # Sample data (replace with your actual data source)
            ["2016", "FEMALE", "ASIAN AND PACIFIC ISLANDER", "Olivia", "172", "1"],
            # ... (more data)
        ]

    def get_page(self, page=1, page_size=10):
        """
        Returns a page of data

        Args:
            page (int, optional): The page number. Defaults to 1.
            page_size (int, optional): The number of items per page. Defaults to 10.

        Returns:
            list: A list of data for the requested page.
        """

        start_index = (page - 1) * page_size
        end_index = start_index + page_size
        return self.data[start_index:end_index]

    def get_hyper(self, page=1, page_size=10):
        """
        Returns a dictionary with hypermedia pagination information

        Args:
            page (int, optional): The page number. Defaults to 1.
            page_size (int, optional): The number of items per page. Defaults to 10.

        Returns:
            dict: A dictionary containing hypermedia pagination information.
        """

        data_page = self.get_page(page, page_size)
        total_data = len(self.data)
        total_pages = ceil(total_data / page_size)  # Calculate total pages

        return {
            "page_size": page_size,
            "page": page,
            "data": data_page,
            "next_page": page + 1 if page < total_pages else None,
            "prev_page": page - 1 if page > 1 else None,
            "total_pages": total_pages,
        }


server = Server()

print(server.get_hyper(1, 2))
print("---")
print(server.get_hyper(2, 2))
print("---")
print(server.get_hyper(100, 3))
print("---")
print(server.get_hyper(3000, 100))
