---
layout: page
title: Slides
permalink: /slides
---

Please find the slides from our dear speakers for your convenience. 


<script>
    (async () => {
    const response = await fetch('https://api.github.com/repos/CloudNativeLinz/cloudnativelinz.github.io/contents/slides');
    const data = await response.json();
    let htmlString = '<ul>';
    
    for (let folder of data) {
        htmlString += `<li><strong>Edition: ${folder.name}</strong></li>`;
        const fileresponse = await fetch('https://api.github.com/repos/CloudNativeLinz/cloudnativelinz.github.io/contents/slides/'+folder.name);
        const filedata = await fileresponse.json();
        htmlString += '<ul>';
        for  (let file of filedata) {
            let mypath = file.path.substring(7); // remove the "slides" from folder structure as it is duplicated
            htmlString += `<li><a href="${mypath}">${file.name}</a></li>`;
        }
        htmlString += '</ul>';
    }

    htmlString += '</ul>';
    document.getElementById('slidecontent').innerHTML = htmlString;
    })()
</script>


<div id="slidecontent">Slides loading...</div>


Note: The list above is rendered directly from the [contents on GitHub](https://github.com/CloudNativeLinz/cloudnativelinz.github.io/tree/main/slides). In case there is any issue, please have a look at the repo itself.
