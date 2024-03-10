// import articles from "../constants/articles"
import axios from 'axios';

/**
 * query the database for a list of articles
 * @param {{string}} query contains the query params
 * @returns articles
 */
const getArticles=async(query)=>{
    let articles = (await axios.get("http://localhost:8000/papers/filterDocuments", {params:query})).data.documents;
    return articles;
}

export default getArticles