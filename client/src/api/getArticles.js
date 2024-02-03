// import articles from "../constants/articles"
import axios from 'axios';
const getArticles=async(query)=>{
    let articles = (await axios.get("http://localhost:8000/papers/filterDocuments", {params:query})).data.documents;
    console.log(query);
    return articles;
}

export default getArticles