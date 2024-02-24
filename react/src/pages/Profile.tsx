import { useDispatch, useSelector } from 'react-redux';
import { fetchUser, selectUser } from '../redux/slices/UserSlice';
import { useEffect } from 'react';
import { selectPets } from '../redux/slices/PetsSlice';

const Profile = () => {
  const dispatch = useDispatch();
  const user = useSelector(selectUser);
  const pets = useSelector(selectPets);

  useEffect(() => {
    dispatch(fetchUser() as any);
  }, [dispatch]);

  return (
    user && (
      <>
        <div>
          {/* todo: add photo */}
          <div>{user.username}</div>
          <div>
            ФИО: {user.name}+ + {user.surname} + {user.patronymic}
          </div>
          <div>Email: {user.email}</div>
        </div>
        {pets && (
          <div>
            {pets.map((item: any) => {
              return pets.name;
            })}
          </div>
        )}
      </>
    )
  );
};

export default Profile;
