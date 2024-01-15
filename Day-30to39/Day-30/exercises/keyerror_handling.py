facebook_posts = eval(input())

total_likes = 0
# Catching the KeyError exception in the dictionary
for post in facebook_posts:
    try:
        total_likes = total_likes + post['Likes']
    except KeyError:
        pass 

print(total_likes)