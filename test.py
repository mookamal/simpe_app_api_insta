import requests as req
def get_user_info(username):
    URL = f"https://www.instagram.com/api/v1/users/web_profile_info/?username={username}"
    headers = {
		"X-Ig-App-Id": "936619743392459"
	}
    response = req.get(URL,headers=headers)
    return response

def edge_followed_by_count(username):
    response = get_user_info(username)
    if response.json():
        return response.json()["data"]["user"]["edge_followed_by"]["count"]


def get_post_info(post_id):
	url = "https://www.instagram.com/api/graphql"

	headers = {
		"Host": "www.instagram.com",
		"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:121.0) Gecko/20100101 Firefox/121.0",
		"Accept": "*/*",
		"Content-Type": "application/x-www-form-urlencoded",
		"X-Ig-App-Id": "936619743392459",
		"X-Fb-Lsd": "AVrGJYNlmwk",
		"X-Asbd-Id": "129477",
		"Sec-Fetch-Site": "same-origin",
	}

	payload = {
		"av": "0",
		"__d": "www",
		"__user": "0",
		"__a": "1",
		"__req": "3",
		"__hs": "19728.HYP%3Ainstagram_web_pkg.2.1..0.0",
		"dpr": "1",
		"__ccg": "UNKNOWN",
		"__rev": "1010699220",
		"__s": "obsyo4%3Akw331n%3Afpievi",
		"__hsi": "7321103255488623607",
		"__dyn": "7xeUjG1mxu1syUbFp60DU98nwgU29zEdEc8co2qwJw5ux609vCwjE1xoswIwuo2awlU-cw5Mx62G3i1ywOwv89k2C1Fwc60AEC7U2czXwae4UaEW2G1NwwwNwKwHw8Xxm16wUwtEvw4JwJwSyES1Twoob82ZwrUdUbGwmk1xwmo6O1FwlE6PhA6bxy4UjxKi",
		"__csr": "iMlElbOk8y28zjVV4NbAAAHvLAizaJ7y8F2axiq-XG54ECC8hUmyAjBCJeFoyax2EyIxFqgRedF3FWkxFqy9eRKeWWml5zFEHjgSh1GQ3aawHxem00j0-rg1zA02Zi06eU7CyP1e260W82lwVJw2rE1f2wOwDwh89U0yi9EE3Uw60S0BpU02GDw",
		"__comet_req": "7",
		"lsd": "AVrGJYNlmwk",
		"jazoest": "21020",
		"__spin_r": "1010699220",
		"__spin_b": "trunk",
		"__spin_t": "1704577183",
		"fb_api_caller_class": "RelayModern",
		"fb_api_req_friendly_name": "PolarisPostActionLoadPostQueryQuery",
        "variables": f'{{"shortcode":"{post_id}","fetch_comment_count":40,"fetch_related_profile_media_count":3,"parent_comment_count":24,"child_comment_count":3,"fetch_like_count":10,"fetch_tagged_user_count":null,"fetch_preview_comment_count":2,"has_threaded_comments":true,"hoisted_comment_id":null,"hoisted_reply_id":null}}',
		"server_timestamps": "true",
		"doc_id": "10015901848480474",
	}

	response = req.post(url, headers=headers, data=payload)
    
	if response.json():
		return response.json()
	else:
		return "Error data"
   
def post_likes_count(post_id):
    data = get_post_info(post_id)
    return data["data"]["xdt_shortcode_media"]["edge_media_preview_like"]["count"]

def post_comments_count(post_id):
    data = get_post_info(post_id)
    return data["data"]["xdt_shortcode_media"]["edge_media_to_parent_comment"]["count"]

print(edge_followed_by_count("m7mad_nor"))