//TO-DO: Write this using React

const contentContainer = document.getElementById("content-container")
const loginForm = document.getElementById('login-form')
const searchForm = document.getElementById('search-form')
const baseEndpoint = "http://localhost:8000/api"

if (loginForm) {
    loginForm.addEventListener('submit', handleLogin)
}

if (searchForm) {
    searchForm.addEventListener('submit', handleSearch)
}

function handleLogin(event) {
    event.preventDefault()
    const loginEndpoint = `${baseEndpoint}/token/`

    let loginFormData = new FormData(loginForm)
    let loginObjectData = Object.fromEntries(loginFormData)
    let bodyStr = JSON.stringify(loginObjectData) 
    // console.log(loginObjectData)

    const options = {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: bodyStr
    }
    fetch(loginEndpoint, options)
    .then(response=>{
        return response.json()
    })
    .then(authData => {
        handleAuthData(authData, getClassList)
    })
    .catch(err=> {
        console.log('err', err)
    })
}

function handleSearch(event) {
    event.preventDefault()
    let formData = new FormData(searchForm)
    let data = Object.fromEntries(formData)
    let searchParams = new URLSearchParams(data) 
    
    const searchEndpoint = `${baseEndpoint}/search/?${searchParams}`
    const headers = {
        "Content-Type": "application/json",
    }

    const authToken = localStorage.getItem('access')
    if (authToken) {
        headers['Authorization'] = `Bearer ${authToken}`
    }

    const options = {
        method: "GET",
        headers: headers
    }
    fetch(searchEndpoint, options)
    .then(response=>{
        return response.json()
    })
    .then(data => {
        const validData = isTokenNotValid(data)
        if (validData && contentContainer) {
            contentContainer.innerHTML = ""
            if (data && data.hits) {
                let htmlStr = ""
                for (let result of data.hits) {
                    htmlStr += "<li>" + result.title + "</li>"
                }
                contentContainer.innerHTML = htmlStr
                if (data.hits.length === 0) {
                    contentContainer.innerHTML = "<p>No results found</p>"
                }
            } else {
                contentContainer.innerHTML = "<p>No results found</p>"
            }
        }
    })
    .catch(err=> {
        console.log('err', err)
    })
}

function handleAuthData(authData, callback) {
    localStorage.setItem('access', authData.access)
    localStorage.setItem('refresh', authData.refresh)

    if (callback) {
        callback()
    }
}

function writeToContainer(data) {
    if (contentContainer) {
        contentContainer.innerHTML = "<pre>" + JSON.stringify(data, null, 4) + "</pre>"
    }
}

function getFetchOptions(method, body) {
    return {
        method: method === null ? "GET" : method,
        headers: {
            "Content-Type": "application/json",
            "Authorization": `Bearer ${localStorage.getItem('access')}`
        },
        body: body ? body : null
    }
}

function isTokenNotValid(jsonData) {
    if (jsonData.code && jsonData.code === "token_not_valid") {
        alert("Please login again")
        return false
    }

    return true
}

function validateJWTToken() {
    const endpoint = `${baseEndpoint}/token/verify/`
    const options = {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            token: localStorage.getItem('access')
        })
    }
    fetch(endpoint, options)
    .then(response=>response.json())
    .then(x=> {
        // refresh token??
    })
}

function getClassList() {
    const endpoint = `${baseEndpoint}/classes/`
    const options = getFetchOptions()
    fetch(endpoint, options)
    .then(response=>{
        return response.json()
    })
    .then(data=> {
        const validData = isTokenNotValid(data)
        
        if (validData) {
            writeToContainer(data)
        }
    })
}


// getClassList()
validateJWTToken()

// copied from here
const searchClient = algoliasearch('FTTPNI3HOI', '7e050b70e43d2882dfa762f2942b8ce5');

const search = instantsearch({
  indexName: 'wendy_Class',
  searchClient,
});

search.addWidgets([
  instantsearch.widgets.searchBox({
    container: '#searchbox',
  }),

    instantsearch.widgets.clearRefinements({
    container: "#clear-refinements"
    }),


instantsearch.widgets.refinementList({
      container: "#user-list",
      attribute: 'user'
  }),
//   instantsearch.widgets.refinementList({
//     container: "#public-list",
//     attribute: 'public'
// }),


  instantsearch.widgets.hits({
    container: '#hits',
    templates: {
        item: `
            <div>
                <div>{{#helpers.highlight}}{ "attribute": "title" }{{/helpers.highlight}}</div>
                <div>{{#helpers.highlight}}{ "attribute": "body" }{{/helpers.highlight}}</div>
                
                <p>{{ schedule }}
                <p>Posted by: {{ user }}</p>
            
            
            </div>`
    }
  })
]);  

search.start();