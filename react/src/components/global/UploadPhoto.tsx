import { useState } from "react";

interface UploadPhotoProps {
  setBase: (base: string) => void
}

const UploadPhoto = (props : UploadPhotoProps) => {

  const [selectedFile, setSelectedFile] = useState<any>(null);
  const [error, setError] = useState<any>(null)

  const handleFileInputChange = (event : any) => {
    const file = event.target.files[0];
    setSelectedFile(file);
    if (file) {
      const reader = new FileReader();
      reader.onloadend = () => {
        let base64String = reader.result as string;
        let s = base64String.split('base64,')
        // bad but ok
        if (s[0].includes('image/')) {
          base64String = s[s.length - 1]
          props.setBase(base64String)
          setError(true)
        } else {
          setError("Некорректное изображение")
        }
      };
      reader.readAsDataURL(file);
    }
  };

  return (
    <div className="file-input-container">
      <input
        type="file"
        id="fileInput"
        className="file-input"
        onChange={handleFileInputChange}
      />
      <label htmlFor="fileInput" className="file-input-label">
        {selectedFile ? selectedFile.name : 'Выберите файл'}
      </label>
      { error && <p className="Error">{error} </p>}
    </div>
  );
};

export default UploadPhoto;