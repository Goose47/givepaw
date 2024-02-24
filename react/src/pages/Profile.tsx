import { useDispatch, useSelector } from 'react-redux';
import { fetchUser, selectUser } from '../redux/slices/UserSlice';
import { useEffect } from 'react';

const Profile = () => {
  const dispatch = useDispatch();
  const user = useSelector(selectUser);

  useEffect(() => {
    dispatch(fetchUser() as any);
  }, [dispatch]);

  return (
    user && (
      <div>
        <div>{user.name}</div>
        <div>{user.surname}</div>
      </div>
    )
  );
};

export default Profile;
