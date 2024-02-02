import { useDispatch } from "react-redux"
import { loginUser } from "../redux/features/userSlice"
import axios from 'axios'

const handleSignUp=async(dispatch,e,email,password,fullname,setIsLoading)=>{
    e.preventDefault();
    console.log("ggg");
    setIsLoading(true);
    try{
        const url = "http://localhost:8000/register";
        console.log(url);
        const user = (await axios.post(url, {fullname,email, password, role:"basic user"})).data.user;
        console.log(user);
        dispatch(loginUser(user));
        } catch (error) {
    // alert(error.response.data.detail);
    } finally {
    setIsLoading(false);
  } 
}
export default handleSignUp