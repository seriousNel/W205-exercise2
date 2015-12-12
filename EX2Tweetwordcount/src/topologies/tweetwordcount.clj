(ns tweetwordcount
  (:use     [streamparse.specs])
  (:gen-class))

(defn tweetwordcount [options]
   [
    ;; Defining three nodes as spouts
    ;; spout configuration
    {"tweet-spout-1" (python-spout-spec
          options
          "spouts.Tweets.Tweets"
          ["tweet"]
          )
	 "tweet-spout-2" (python-spout-spec
          options
          "spouts.Tweets.Tweets"
          ["tweet"]
          )
	"tweet-spout-3" (python-spout-spec
          options
          "spouts.Tweets.Tweets"
          ["tweet"]
          )
    }
    ;; bolt configuration 1
	;; The first parse bolt receives the tweets from first and second spouts  
    {"parse-tweet-bolt-1" (python-bolt-spec
          options
          {"tweet-spout-1" :shuffle
		   "tweet-spout-2" :shuffle}
          "bolts.Parse.ParseTweet"
          ["word"]
          :p 2
          )
	;; The second sparse bolt receives the tweets from all the spouts 
	"parse-tweet-bolt-2" (python-bolt-spec
          options
          {"tweet-spout-1" :shuffle
		   "tweet-spout-2" :shuffle
		   "tweet-spout-3" :shuffle}
          "bolts.Parse.ParseTweet"
          ["word"]
          :p 2
          )
	;; The third sparse bolt receives the tweets from the third spout only
     "parse-tweet-bolt-3" (python-bolt-spec
          options
          {"tweet-spout-3" :shuffle}
          "bolts.Parse.ParseTweet"
          ["word"]
          :p 2
          )		  
	;; bolt configuration 2
	;; The first count bolt receives the tweet words from allthe three sparse bolts
     "count-bolt-1" (python-bolt-spec
          options
          {"parse-tweet-bolt-1" ["word"]
		   "parse-tweet-bolt-2" ["word"]
		   "parse-tweet-bolt-3" ["word"]
		  }
          "bolts.Wordcount.WordCounter"
          ["word" "count"]
          :p 2
          )
	;; The second count bolt receives the tweet words from parse bolts 1 and 2
	"count-bolt-2" (python-bolt-spec
          options
          {"parse-tweet-bolt-1" ["word"]
		   "parse-tweet-bolt-2" ["word"]
		  }
          "bolts.Wordcount.WordCounter"
          ["word" "count"]
          :p 2
          )
    }
  ]
)
