// import articles from "../constants/articles"
import axios from 'axios';
const getArticles=async(query)=>{
    let articles = (await axios.get("http://localhost:8000/papers/filterDocuments", query)).data.documents;
    console.log(articles);
    return articles;
}

export default getArticles