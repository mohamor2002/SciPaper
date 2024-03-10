import { useDispatch } from "react-redux"
import { loginUser } from "../redux/features/userSlice"
import axios from 'axios'


/**
 * sign up user
 * @param {*} dispatch dispatch the state of the signed up user
 * @param {React.MouseEvent} e 
 * @param {string} email 
 * @param {string} password 
 * @param {string} fullname 
 * @param {function} setIsLoading
 */

const handleSignUp=async(dispatch,e,email,password,fullname,setIsLoading)=>{
    e.preventDefault();
    setIsLoading(true);
    try{
        const url = "http://localhost:8000/register";
        console.log(url);
        const user = (await axios.post(url, {fullname,email, password, role:"basic user"}, {withCredentials:true})).data.user;
        console.log(user);
        dispatch(loginUser(user));
        } catch (error) {
    // alert(error.response.data.detail);
    } finally {
    setIsLoading(false);
  } 
}
export default handleSignUp