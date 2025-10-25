import { useEffect, useState } from 'react'
import BottomNavigation from '@mui/material/BottomNavigation';
import BottomNavigationAction from '@mui/material/BottomNavigationAction';
import HomeIcon from '@mui/icons-material/Home';
import SettingsIcon from '@mui/icons-material/Settings';
import FaceIcon from '@mui/icons-material/Face';
import { Link, useNavigate } from 'react-router';

export const NavBar = () => {
    const navigate = useNavigate();
    const [value, setValue] = useState(location.pathname)

    const handleChange = (event, newValue) => {
        navigate(newValue);
        setValue(location.pathname);
    };

    return (
        <BottomNavigation sx={{ width: '100%' }} value={value} onChange={handleChange}>
            <BottomNavigationAction 
                label="Profile" 
                value="/profile" 
                icon={<FaceIcon />} 
                component={Link}
                to = "/profile"
            />
            <BottomNavigationAction
                label="Home"
                value="/home"
                icon={<HomeIcon />}
                component={Link}
                to="/"
            />
            <BottomNavigationAction
                label="Settings"
                value="/setting"
                icon={<SettingsIcon />}
                component={Link}
                to="/settings"
            />
        </BottomNavigation>
    );
}