import {useEffect, useRef, useState} from 'react'
import {useDispatch, useSelector} from 'react-redux'
import {NavLink, useNavigate} from 'react-router-dom'
import {getUserDetails} from '../features/user/userAction'
import {logout} from '../features/user/userSlice'
import '../styles/header.css'

const Header = () => {
    const {userInfo, userToken} = useSelector((state) => state.user)
    const dispatch = useDispatch()
    const navigate = useNavigate()
    const catMenu = useRef(null)

    const [open, setOpen] = useState(false);

    const menuItems = ["Profile", "Log Out"]

    // automatically authenticate user if token is found
    useEffect(() => {
        if (userToken) {
            dispatch(getUserDetails())
        }
    }, [userToken, dispatch])

    const closeOpenMenus = (e) => {
        if (catMenu.current && open && !catMenu.current.contains(e.target)) {
            setOpen(false)
        }
    }

    document.addEventListener('mousedown', closeOpenMenus)

    const handleOpen = () => {
        setOpen(!open);
    };

    const handleDropDown = (item) => {
        if (item === "Profile") {
            navigate("/user-profile")
        } else if (item === "Log Out") {
            dispatch(logout())
            setOpen(false)
            navigate("/")
        }
    };


    return (
        <header>
            <div className='header-status'>
                <img className="logo" onClick={() => navigate("/")} src="main_logo.jpg" alt="Logo"/>
                <div className="navigation">
                    <NavLink to="/">Text</NavLink>
                    <NavLink to="/">Text</NavLink>
                    <NavLink to="/">Text</NavLink>
                </div>
                {userToken ? (<div className="userIcon">
                    <div ref={catMenu} className="dropdown">
                        <img onClick={handleOpen} src="usericon.png" alt="UserIcon"/>
                        {open ? (
                            <ul className="menu">
                                {menuItems.map((item) => (<li className="menu-item">
                                    <button className="item-text" onClick={() => handleDropDown(item)}>{item}</button>
                                </li>))}
                            </ul>
                        ) : null}
                    </div>
                </div>) : (<div className='userIcon'>
                    <NavLink className='button' to='/login'>
                        Login
                    </NavLink>
                </div>)}
            </div>
        </header>
    )
}
export default Header