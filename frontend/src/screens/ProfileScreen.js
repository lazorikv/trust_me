import { useSelector } from 'react-redux'
import '../styles/profile.css'

const ProfileScreen = () => {


  const { userInfo } = useSelector((state) => state.user)
  return (
    <div>
      <figure>{userInfo.first_name}</figure>
      <span>
        Welcome <strong>{userInfo.first_name}!</strong> You can view this page
        because you're logged in
      </span>
    </div>
  )
}
export default ProfileScreen