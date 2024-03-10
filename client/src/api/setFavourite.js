import axios from 'axios';


/**
 * add an article to favourites or remove it
 * @param {React.MouseEvent} e button event 
 * @param {string} id the article id
 * @param {string} option ['add', 'remove'] used to determine whether to add to favorties or to remove
 */
const setFavourite=async(e,id, option)=>{
    e.preventDefault()
    console.log(555);
    if(option === 'add'){
        await axios.post('http://localhost:8000/addFavorite', {'id':id}, {withCredentials:true});
    }
    else{
        await axios.post('http://localhost:8000/removeFavorite', {'id':id}, {withCredentials:true});
    }
}
export default setFavourite