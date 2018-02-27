import tweepy

def get_api(cfg):
  auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
  auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
  return tweepy.API(auth)

def main():
  # Fill in the values noted in previous step here
  cfg = { 
    "consumer_key"        : "IrQcPnoAwMMoxeXaXMzzvR72E",
    "consumer_secret"     : "cDZxcCxJIviqf4DvSKdDHwIOeeNjlAG5TSIBTvWFXqdqvB38xc",
    "access_token"        : "967252345133457409-Y7LtFVq1yucs1vszqba3reTpWyZvRkH",
    "access_token_secret" : "KtGHo9V6lB8KAGXCj8hgfhuX4s1vgif00SJdMcwO1K0ro" 
    }

  api = get_api(cfg)
  tweet = "IM DEVESH,THE LEGEND!"
  status = api.update_status(status=tweet) 
  # Yes, tweet is called 'status' rather confusing

if __name__ == "__main__":
  main()
