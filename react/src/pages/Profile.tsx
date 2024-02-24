import { useDispatch, useSelector } from 'react-redux';
import { fetchUser, selectUser } from '../redux/slices/UserSlice';
import { useEffect } from 'react';
import { fetchPets, selectPets } from '../redux/slices/PetsSlice';

const Profile = () => {
  const dispatch = useDispatch();
  const user = useSelector(selectUser);
  const pets = useSelector(selectPets);

  useEffect(() => {
    dispatch(fetchUser() as any);
    dispatch(fetchPets() as any);
  }, [dispatch]);

  return (
    user && (
      <>
        <div>
          {/* todo: add photo */}
          <div>{user.username}</div>
          <div>ФИО: {user.name + ' ' + user.surname + ' ' + user.patronymic}</div>
          <div>Email: {user.email}</div>
        </div>
        <div>
          {pets.map((pet: any) => (
            <div key={pet.id}>
              {/* <img src={pet.avatar.photo_thumb} alt={pet.name} /> */}
              <div>{pet.name}</div>
              <div>Возраст: {pet.age}</div>
              <div>Вес: {pet.weight}</div>
              <div>Порода: {pet.breed}</div>
            </div>
          ))}
        </div>
      </>
    )
  );
};

export default Profile;
