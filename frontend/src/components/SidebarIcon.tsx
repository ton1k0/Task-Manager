
import {IconButton} from "@chakra-ui/react";
import React from "react";

interface ISidebarIconProps {
    icon : React.ReactElement
}

export function SidebarIcon({icon}:ISidebarIconProps) {
    return(
        <IconButton
            _hover={{
                background: "white",
            }}
            colorScheme='purple'
            aria-label='SidebarIcon'
            height='50px'
            width='50px'
            variant='ghost'
            icon={icon}>
        </IconButton>
    )
}