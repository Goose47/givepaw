import { useDispatch, useSelector } from 'react-redux';
import { fetchUser, selectUser } from '../redux/slices/UserSlice';

const ProfileEdit = () => {
    const user = useSelector(selectUser);

    return(<div>
            
    </div>)


}

export default ProfileEdit;