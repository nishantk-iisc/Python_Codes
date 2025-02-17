import requests

for i in range(1, 28):
	url = f"https://cse.iitk.ac.in/users/piyush/courses/ml_autumn16/771A_lec{i}_slides.pdf"
	response = requests.get(url)

	if response.status_code == 200:
	    with open(f"771A_lec{i}_slides.pdf", "wb") as file:
	        file.write(response.content)
	    print("PDF downloaded successfully.")
	else:
	    print(f"Failed to download PDF. Status code: {response.status_code}")

