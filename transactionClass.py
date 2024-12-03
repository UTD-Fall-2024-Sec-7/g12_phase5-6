import http.client
import ssl
import json

class transactionClass:
    def __init__(self):
        self.context = ssl._create_unverified_context()  # Bypass SSL verification
        self.conn = http.client.HTTPSConnection("api.quiverquant.com", context=self.context)
        self.headers = {
            'Accept': "application/json",
            'Authorization': "Bearer 8811e9c3ec80c57c79b915490ff666da60e3b888"
        }

    def get_recent_trades(self, congressman_name):
        """
        Fetches the 5 most recent trades for a given congressman, with handling for throttling.
        """
        try:
            representative = congressman_name.replace(" ", "+")
            self.conn.request(
                "GET",
                f"/beta/bulk/congresstrading?page=1&page_size=100&representative={representative}",
                headers=self.headers
            )
            res = self.conn.getresponse()
            data = res.read()

            # Parse JSON response
            trades = json.loads(data.decode("utf-8"))

            # Check for throttling response
            if isinstance(trades, dict) and 'detail' in trades and 'throttled' in trades['detail'].lower():
                print(f"Throttling detected for {congressman_name}: {trades['detail']}")
                return {"error": "throttled", "message": trades['detail']}  # Return a throttling indicator

            # Ensure that trades are dictionaries
            if isinstance(trades, list):
                return trades  # Return parsed list of dictionaries
            else:
                print(f"Unexpected response format for {congressman_name}: {trades}")
                return []

        except Exception as e:
            print(f"Error fetching trades for {congressman_name}: {e}")
            return []



    def interactive_query(self):
        """
        Allows the user to query the API interactively for trades by entering a ticker and congressman name.
        """
        print("\n--- Interactive Query ---")
        ticker = input("Enter the ticker (leave blank if not needed): ")
        representative = input("Enter the representative's name (leave blank if not needed): ")
        representative = representative.replace(" ", "+")

        # Build the request
        self.conn.request(
            "GET",
            f"/beta/bulk/congresstrading?page=10&page_size=10&representative={representative}&ticker={ticker}",
            headers=self.headers
        )

        res = self.conn.getresponse()
        data = res.read()

        print("\n--- Query Results ---")
        print(data.decode("utf-8"))

    def get_stocks_for_congressman(self, congressman_name):
        """
        Fetches stock data related to a given congressman by querying their trades.
        """
        try:
            # Replace spaces in the congressman name with '+'
            representative = congressman_name.replace(" ", "+")
            self.conn.request(
                "GET",
                f"/beta/bulk/congresstrading?page=10&page_size=5&representative={representative}",
                headers=self.headers
            )

            res = self.conn.getresponse()
            data = res.read()
            trades = json.loads(data.decode("utf-8"))

            # Transform the response into stock-specific data
            stocks = []
            for trade in trades:
                stock_info = {
                    "symbol": trade.get("Ticker", "N/A"),
                    "price": trade.get("Amount", 0.0),
                    "change": self.calculate_change(trade)  # Placeholder for percentage change logic
                }
                stocks.append(stock_info)

            return stocks
        except Exception as e:
            print(f"Error fetching stocks for {congressman_name}: {e}")
            return []

    def calculate_change(self, trade):
        """
        Placeholder method to calculate the percentage change of a stock (mock data).
        """
        # Replace with actual logic if available; here, we just return a random change.
        import random
        return round(random.uniform(-2.0, 2.0), 2)
