import {BrowserRouter as Router, Routes, Route} from 'react-router-dom'
import Header from './components/Header'
import LoginScreen from './screens/LoginScreen'
import RegisterScreen from './screens/RegisterScreen'
import ProfileScreen from './screens/ProfileScreen'
import HomeScreen from './screens/home/HomeScreen'
import ProtectedRoute from './features/user/ProtectedRoute'
import './App.css'
import {Footer} from "./components/Footer";

function App() {
    return (
        <Router>
            <Header/>
            <main className='content'>
                <Routes>
                    <Route path='/' element={<HomeScreen/>}/>
                    <Route path='/login' element={<LoginScreen/>}/>
                    <Route path='/register' element={<RegisterScreen/>}/>
                    <Route element={<ProtectedRoute/>}>
                        <Route path='/user-profile' element={<ProfileScreen/>}/>
                    </Route>
                </Routes>
            </main>
            <Footer/>
        </Router>
    )
}

export default App