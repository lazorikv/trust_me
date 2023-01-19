import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Header from "./components/Header";
import LoginScreen from "./screens/LoginScreen";
import RegisterScreen from "./screens/RegisterScreen";
import ProfileScreen from "./screens/ProfileScreen";
import HomeScreen from "./screens/home/HomeScreen";
import ApartmentsScreen from "./screens/apartments/apartments";
import ProtectedRoute from "./features/user/ProtectedRoute";
import "./App.css";
import { Footer } from "./components/Footer";
import Apartment from "./screens/apartments/getapartment/Apartment";
import { ScrollToTop } from "./app/utils";

function App() {
  return (
    <Router>
      <Header />
      <main className="content">
        <ScrollToTop />
        <Routes>
          <Route path="/" element={<HomeScreen />} />
          <Route path="/login/" element={<LoginScreen />} />
          <Route path="/register/" element={<RegisterScreen />} />
          {/*<Route element={<ProtectedRoute />}>*/}
          <Route path="/user-profile/" element={<ProfileScreen />} />
          <Route path="/apartments/" element={<ApartmentsScreen />} />
          {/*</Route>*/}
          <Route path="/apartments/:apartment_id/" element={<Apartment />} />
        </Routes>
      </main>
      <Footer />
    </Router>
  );
}

export default App;
