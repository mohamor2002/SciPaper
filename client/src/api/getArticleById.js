import articles from "../constants/articles"
import axios from 'axios';

const getArticleById=async(id,setArticle,setIsFavourite)=>{
    const article= (await axios.get(`http://localhost:8000/papers/getDocuments`,{params : {'id':[id]}})).data.documents[0];
    setArticle(article)
    console.log(article)
    setIsFavourite(article.isFavourite)
}
export default getArticleById