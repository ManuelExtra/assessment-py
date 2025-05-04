from jsonplaceholder.client import JsonPlaceholder
import json  # Add this import at the top

def run_demo():
    """Demonstrate the functionality of the JsonPlaceholder class."""
    api = JsonPlaceholder()

    # Task 1: Retrieve all posts
    print("\n=== Task 1: Retrieve all posts ===")
    posts = api.get_all_posts()
    if posts:
        print(f"Total number of posts: {len(posts)}")

    # Task 2: Retrieve post #10
    print("\n=== Task 2: Retrieve post #10 ===")
    post_10 = api.get_post(10)
    if post_10:
        print(f"Title of post #10: {post_10['title']}")
        print(f"Body of post #10: {post_10['body']}")

    # Task 3: Retrieve all posts from User ID 7
    print("\n=== Task 3: Retrieve all posts from User ID 7 ===")
    user_7_posts = api.get_posts_by_user(7)
    if user_7_posts:
        print(f"Number of posts by user 7: {len(user_7_posts)}")

    # Task 4: Get all comments from Post 8 and update them
    print("\n=== Task 4: Get all comments from Post 8 and update them ===")
    comments = api.get_comments_for_post(8)
    if comments:
        for comment in comments:
            # Swap name and email
            new_name = comment['email']
            new_email = comment['name']
            comment['name'] = new_name
            comment['email'] = new_email
            
            # Convert back to JSON string
            updated_comment_json = json.dumps(comment)
            print(f"Updated comment JSON: {updated_comment_json}")
            
            # Update via PUT
            update_response = api.update_comment(comment['id'], comment)
            if update_response:
                print(f"Successfully updated comment {update_response['id']}")

    # Task 5: Attempt to get post 101
    print("\n=== Task 5: Attempt to get post 101 ===")
    post_101 = api.get_post(101)
    if post_101:
        print(f"Title of post 101: {post_101['title']}")
    else:
        print("Post 101 not found (expected behavior)")


if __name__ == "__main__":
    run_demo()