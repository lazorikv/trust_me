import { useForm } from "react-hook-form";
import { useNavigate } from "react-router-dom";
import { useDispatch, useSelector } from "react-redux";
import { getUserDetails, userLogin } from "../features/user/userAction";
import { useEffect, useState } from "react";
import Error from "../components/Error";

const LoginScreen = () => {
  const { loading, userInfo, error } = useSelector((state) => state.user);
  const dispatch = useDispatch();
  const { register, handleSubmit } = useForm();
  const navigate = useNavigate();
  const [role, setRole] = useState("Select");

  // redirect authenticated user to profile screen
  useEffect(() => {
    if (userInfo) {
      dispatch(getUserDetails());
      navigate("/user-profile/");
    }
  }, [navigate, userInfo]);

  const submitForm = (data) => {
    dispatch(userLogin(data));
  };

  const handleRegisterClick = () => {
    navigate("/register/");
  };

  return (
    <form onSubmit={handleSubmit(submitForm)}>
      {error && <Error>{error}</Error>}
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
      <button type="submit" className="button" disabled={loading}>
        Login
      </button>
      <button
        className="button"
        onClick={handleRegisterClick}
        disabled={loading}
      >
        Register
      </button>
    </form>
  );
};
export default LoginScreen;
