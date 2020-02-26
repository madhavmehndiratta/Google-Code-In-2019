const NEWS_TOPICS = 'Linux OR Open-Source OR Android'
const API_KEY = '6e47ec0603cc45e09aefcecba94fc2a8'

fetch(`https://newsapi.org/v2/everything?q=${NEWS_TOPICS}&apiKey=${API_KEY}&language=en`)
    .then((response) => {
        return response.json();
    })
    .then((JSON) => {
        const article = JSON['articles'];
        console.log(article);

        for (let i = 0; i < article.length; ++i) {
            const article_box = document.getElementById(i);

            const title_div = document.createElement('div')
            title_div.className = 'grid-item-title'
            const title = document.createElement('h2');
            const node = document.createTextNode(article[i]['title']);
            title.appendChild(node)
            title_div.appendChild(title)
            article_box.appendChild(title_div);

            const image_div = document.createElement('div')
            image_div.className = 'grid-item-img'
            const image = document.createElement('img')
            image.src = article[i]['urlToImage'];
            image_div.appendChild(image);
            article_box.appendChild(image_div);

            const description_div = document.createElement('div');
            description_div.className = 'grid-item-description';
            const description = document.createElement('p');
            const desc = document.createTextNode(article[i]['description']);
            description.appendChild(desc);
            description_div.appendChild(description);
            article_box.appendChild(description_div);

            const click_div = document.createElement('div');
            click_div.className = 'grid-item-click';
            const click = document.createElement('a');
            click.href = article[i]['url'];
            const read_more = document.createTextNode('Read More ...');
            click.appendChild(read_more);
            click_div.appendChild(click);
            article_box.appendChild(click_div);
        }
    })