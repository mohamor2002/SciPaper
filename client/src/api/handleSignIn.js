import { useDispatch } from "react-redux"
import { loginUser } from "../redux/features/userSlice"
import axios from 'axios'
import Cookies from 'js-cookie';



/**
 * sign in a user
 * @param {*} dispatch 
 * @param {string} email 
 * @param {React.MouseEvent} e 
 * @param {string} password 
 * @param {string} setIsLoading 
 */
const handleSignIn=async(dispatch,email,e,password,setIsLoading)=>{
    e.preventDefault();
    console.log("fff")
    setIsLoading(true);
    try{
        const url = "http://localhost:8000/login";
        const resp = (await axios.post(url, {username:email, password}, {withCredentials:true}))
        const user = resp.data.user;

        // let name = resp.data.cookieName;
        // let value = resp.data.cookieValue;
        // Cookies.set(name, value);
        dispatch(loginUser(user));
        } catch (error) {
    // alert(error.response.data.detail);
    } finally {
    setIsLoading(false);
  }
};
export default handleSignIn