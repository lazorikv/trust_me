import { useEffect, useRef, useState } from "react";
import { useForm } from "react-hook-form";
import { useDispatch, useSelector } from "react-redux";
import { useNavigate } from "react-router-dom";
import Error from "../components/Error";
import { getUserDetails, registerUser } from "../features/user/userAction";
import { logout } from "../features/user/userSlice";

const RegisterScreen = () => {
  const { loading, userInfo, error, success } = useSelector(
    (state) => state.user
  );
  const dispatch = useDispatch();
  const { register, handleSubmit } = useForm();
  const [role, setRole] = useState("Select");

  const navigate = useNavigate();

  useEffect(() => {
    // redirect user to login page if registration was successful
    if (success) navigate("/login/");
    // redirect authenticated user to profile screen
    if (userInfo) navigate("/user-profile/");
  }, [navigate, userInfo, success]);

  const submitForm = (data) => {
    // check if passwords match
    if (data.password !== data.confirmPassword) {
      alert("Password mismatch");
      return;
    }
    // transform email string to lowercase to avoid case sensitivity issues in login
    data.email = data.email.toLowerCase();
    dispatch(registerUser(data));
  };

  return (
    <form onSubmit={handleSubmit(submitForm)}>
      <div className="form-group">
        <label htmlFor="firstName">First Name</label>
        <input
          type="text"
          className="form-input"
          {...register("first_name")}
          required
        />
      </div>
      <div className="form-group">
        <label htmlFor="firstName">Last Name</label>
        <input
          type="text"
          className="form-input"
          {...register("last_name")}
          required
        />
      </div>
      <div className="form-group">
        <label htmlFor="firstName">Phone Number</label>
        <input
          type="text"
          className="form-input"
          {...register("phone_number")}
          required
        />
      </div>
      <div className="form-group">
        <label htmlFor="email">Email</label>
        <input
          type="email"
          className="form-input"
          {...register("email")}
          required
        />
      </div>
      <div className="form-group">
        <label htmlFor="password">Password</label>
        <input
          type="password"
          className="form-input"
          {...register("password")}
          required
        />
      </div>
      <div className="form-group">
        <label htmlFor="email">Confirm Password</label>
        <input
          type="password"
          className="form-input"
          {...register("confirmPassword")}
          required
        />
      </div>
      <div className="form-group">
        <label htmlFor="firstName">Role</label>
        <select
          className="form-input"
          {...register("role")}
          required
          value={role}
          onChange={(e) => setRole(e.target.value)}
        >
          <option value="landlord">Landlord</option>
          <option value="tenant">Tenant</option>
        </select>
      </div>
      <button type="submit" className="button">
        Register
      </button>
    </form>
  );
};

export default RegisterScreen;
