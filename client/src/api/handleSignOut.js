import { logoutUser } from "../redux/features/userSlice"
import axios from 'axios';



/**
 * sign out a user
 * @param {*} e 
 * @param {*} dispatch 
 */
const handleSignOut=async(e,dispatch)=>{
    e.preventDefault()
    try{
        const url = "http://localhost:8000/logout";
        await axios.post(url,{}, {withCredentials:true});
        dispatch(logoutUser())
    }
    catch(error){}
}
export default handleSignOut