from jsonplaceholder.client import JsonPlaceholder
import json


def run_main():
    """Demonstrate all required functionality."""
    api = JsonPlaceholder()

    # Success Criteria 1: Retrieve all posts
    print("\n=== 1. Retrieve all posts ===")
    posts_data, _ = api.get_all_posts()
    if posts_data:
        print(f"1a. Total posts: {len(posts_data)}")

    # Success Criteria 2: Retrieve post #10
    print("\n=== 2. Retrieve post #10 ===")
    post_10_data, post_10_headers = api.get_post(10)
    if post_10_data:
        print(f"2a. Title of post #10: {post_10_data['title']}")
        # Note: The API doesn't return encoding property in response body
        print("2b. Encoding property not returned by this API")
        if post_10_headers:
            print(f"2c. X-Powered-By: {post_10_headers.get('X-Powered-By', 'Not available')}")

    # Success Criteria 3: Retrieve all posts from User ID 7
    print("\n=== 3. Retrieve all posts from User ID 7 ===")
    user_7_posts, _ = api.get_posts_by_user(7)
    if user_7_posts:
        print(f"3a. Number of posts by user 7: {len(user_7_posts)}")

    # Success Criteria 4: Get all comments from Post 8
    print("\n=== 4. Get all comments from Post 8 ===")
    comments_data, _ = api.get_comments_for_post(8)
    if comments_data:
        print(f"4a. Retrieved {len(comments_data)} comments")
        for comment in comments_data:
            # 4b.i: Swap name and email
            name = comment['name']
            email = comment['email']
            comment['name'] = email
            comment['email'] = name
            
            # 4b.ii-iii: Convert to JSON and print
            updated_comment_json = json.dumps(comment, indent=2)
            print(f"\n4b.ii-iii. Updated comment JSON:\n{updated_comment_json}")
            
            # 4b.iv-v: Update via PUT
            update_response, _ = api.update_comment(comment['id'], comment)
            if update_response:
                print(f"4b.v. Successfully updated comment ID: {update_response['id']}")

    # Success Criteria 5: Attempt to get post 101
    print("\n=== 5. Attempt to get post 101 ===")
    post_101, _ = api.get_post(101)
    if post_101:
        print(f"Title of post 101: {post_101['title']}")
    else:
        print("Post 101 not found (as expected)")


if __name__ == "__main__":
    run_main()