import axios from 'axios';

export const getBreeds = async () => {
  try {
    const response = await axios.get('pets/breeds');
    return response.data;
  } catch (error) {
    console.error(error);
  }
};

export const getBloodTypes = async (pet_type_id: number) => {
  try {
    const response = await axios.get(`blood_group/${pet_type_id}`);
    return response.data;
  } catch (error) {
    console.error(error);
  }
};
export const getVaccines = async () => {
  try {
    const response = await axios.get('pets/vaccinations');
    return response.data;
  } catch (error) {
    console.error(error);
  }
};

export const getAnimalTypes = async () => {
  try {
    const response = await axios.get('pets/pet_types');
    return response.data;
  } catch (error) {
    console.error(error);
  }
};

export const veterinaryClinics = async () => {
  try {
    const response = await axios.get('');
    return response.data;
  } catch (error) {
    console.error(error);
  }
};

export const sendDonor = async () => {
  try {
    const response = await axios.post('donors');
    return response.data;
  } catch (error) {
    console.error(error);
  }
};

export const sendRecipient = async (reason: string) => {
  try {
    const response = await axios.post('recipients');
    return response.data;
  } catch (error) {
    console.error(error);
  }
};

// ADD AXIOS URL
export const getPets = async () => {
  try {
    const response = await axios.get('pets/my');
    return response.data;
  } catch (error) {
    console.error(error);
  }
};
