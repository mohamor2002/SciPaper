import axios from 'axios';


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