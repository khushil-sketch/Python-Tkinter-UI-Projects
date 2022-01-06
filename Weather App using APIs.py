from tkinter import *
import json
import requests

root = Tk()
root.title('Air Quality App ')
root.geometry('510x180')
root.configure(background='#4d004d')
# Davis zipcode: 95616, distance: 5 miles
# Sacramento: 95821

try:
    # GETTING & PARSING JSON DATA
    api_request = requests.get(
        "https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=95616&distance=5&API_KEY=INSERT API KEY HERE")
    # print(api_request.content) #Prints the content of whatever requests gets from the API. So, it prints the raw JSON string because we havent parsed it yet.
    api = json.loads(api_request.content)  # parses the JSON string into a Python dictionary
    # Note: Parameter 03 means Ozone. The site doesn't say it, but the guy in the tutorials says it.

    # INDICES
    date = api[0]["DateObserved"]
    area = api[0]["ReportingArea"]
    state = api[0]["StateCode"]
    aqi_val = api[0]["AQI"]
    category = api[0]["Category"]["Name"]

    # LABELS
    date_l = Label(root, text="Date: " + date + "\n" + area + ", " + state, font=('System', 14), bg="#ff0066")
    date_l.grid(row=0, column=1, sticky='WE', ipady=10, ipadx=2, padx=(20), pady=(20, 0))

    empty_l = Label(root, text=" ", bg='#4d004d')
    empty_l.grid(row=1, column=4)

    category_l = Label(root, text="Air Quality: " + str(category) + " [Value:" + str(aqi_val) + "]",
                       font=('Fixedsys', 20), bg="#00ffff")
    category_l.grid(row=2, column=0, columnspan=3, sticky='WE', ipady=10, ipadx=10, padx=(20))

except Exception as error:
    print(error)

########################################################################################
# Use this if you want to see how the foratted JSON data looks like:
# print(json.dumps(api, indent=2))
# print(json.dumps(api_request)) #Doesn't work, Python says its not JSON serializable, meaning we can't convert it to a string,
# since the data api_requests contains is already a string.

# Use if you want to just see the data, unformatted:
# print(api)

# Leave this
root.mainloop()
