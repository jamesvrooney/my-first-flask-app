from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
posts = {
    0: {
        "post_id": 0,
        "title": "Hello World",
        "content": "Hello to everyone in the world"
    },
    1: {
        "post_id": 1,
        "title": "Hello Jeter",
        "content": "Hello to every Jeter in the world"
    }
}


@app.route('/')
def home():
    return render_template('home.html', posts=posts)


@app.route('/post/<int:post_id>')
def getPost(post_id):
    post = posts.get(post_id)

    if not post:
        return render_template('404.html', message=f"Sorry! A post with id {post_id} was not found.")

    return render_template('post.html', post=posts[post_id])


# @app.route('/post/form')
# def createPostForm():
#     return render_template('create_post.html')
#

@app.route('/post/create', methods=['GET', 'POST'])
def createPost():
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        post_id = len(posts)

        posts[post_id] = {"post_id": post_id, 'title': title, 'content': content}

        return redirect(url_for('getPost', post_id=post_id))

    return render_template('create_post.html')


if __name__ == '__main__':
    app.run(debug=True)
