import articles from "../constants/articles"
import axios from 'axios';


/**
 * 
 * @param {string} id the id of the required article
 * @param {function} setArticle 
 * @param {function} setIsFavourite 
 */
const getArticleById=async(id,setArticle,setIsFavourite)=>{
    const article= (await axios.get(`http://localhost:8000/papers/getDocuments`,{params : {'id':[id]}})).data.documents[0];
    setArticle(article)
    console.log(article)
    setIsFavourite(article.isFavourite)
}
export default getArticleById