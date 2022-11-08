from website import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True) #rerun when we make a change in any python code