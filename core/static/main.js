function q(selector) {
    return document.querySelector(selector)
}

function main() {
    noResults()
}

function noResults() {
    if snippets {
    } else {
        q(body).innerHTML = <p>Sorry, your search returned zero results.</p>
    }
}

document.addEventListener('DOMContentLoaded', function () {
    main()
})

