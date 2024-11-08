const defaultTheme = require('tailwindcss/defaultTheme');

/** @type {import('tailwindcss').Config} */
module.exports = {
    content: [
        "./templates/**/*.{html,htm,jinja}",
        "./components/**/*.{html,htm,jinja}",
        "./static/src/**/*.js"
    ],
    theme: {
        extend: {
            colors: {
                'surface': 'rgb(var(--surface) / <alpha-value>)',
                'surface-variant': 'rgb(var(--surface-variant) / <alpha-value>)',
                'on-surface': 'rgb(var(--on-surface) / <alpha-value>)',
                'on-surface-variant': 'rgb(var(--on-surface-variant) / <alpha-value>)',
                'primary': 'rgb(var(--primary) / <alpha-value>)',
                'secondary': 'rgb(var(--secondary) / <alpha-value>)',
                'tertiary': 'rgb(var(--tertiary) / <alpha-value>)',
                'error': 'rgb(var(--error) / <alpha-value>)',
                'on-primary': 'rgb(var(--on-primary) / <alpha-value>)',
                'on-secondary': 'rgb(var(--on-secondary) / <alpha-value>)',
                'on-tertiary': 'rgb(var(--on-tertiary) / <alpha-value>)',
                'on-error': 'rgb(var(--on-error) / <alpha-value>)',
                'primary-container': 'rgb(var(--primary-container) / <alpha-value>)',
                'secondary-container': 'rgb(var(--secondary-container) / <alpha-value>)',
                'tertiary-container': 'rgb(var(--tertiary-container) / <alpha-value>)',
                'error-container': 'rgb(var(--error-container) / <alpha-value>)',
                'on-primary-container': 'rgb(var(--on-primary-container) / <alpha-value>)',
                'on-secondary-container': 'rgb(var(--on-secondary-container) / <alpha-value>)',
                'on-tertiary-container': 'rgb(var(--on-tertiary-container) / <alpha-value>)',
                'on-error-container': 'rgb(var(--on-error-container) / <alpha-value>)',
                'background': 'rgb(var(--background) / <alpha-value>)',
                'on-background': 'rgb(var(--on-background) / <alpha-value>)',
                'outline': 'rgb(var(--outline) / <alpha-value>)',
                'outline-variant': 'rgb(var(--outline-variant) / <alpha-value>)',
                'shadow': 'rgb(var(--shadow) / <alpha-value>)',
                'scrim': 'rgb(var(--scrim) / <alpha-value>)',
                'inverse-surface': 'rgb(var(--inverse-surface) / <alpha-value>)',
                'inverse-on-surface': 'rgb(var(--inverse-on-surface) / <alpha-value>)',
                'inverse-primary': 'rgb(var(--inverse-primary) / <alpha-value>)',
                'primary-fixed': 'rgb(var(--primary-fixed) / <alpha-value>)',
                'on-primary-fixed': 'rgb(var(--on-primary-fixed) / <alpha-value>)',
                'primary-fixed-dim': 'rgb(var(--primary-fixed-dim) / <alpha-value>)',
                'on-primary-fixed-variant': 'rgb(var(--on-primary-fixed-variant) / <alpha-value>)',
                'secondary-fixed': 'rgb(var(--secondary-fixed) / <alpha-value>)',
                'on-secondary-fixed': 'rgb(var(--on-secondary-fixed) / <alpha-value>)',
                'secondary-fixed-dim': 'rgb(var(--secondary-fixed-dim) / <alpha-value>)',
                'on-secondary-fixed-variant': 'rgb(var(--on-secondary-fixed-variant) / <alpha-value>)',
                'tertiary-fixed': 'rgb(var(--tertiary-fixed) / <alpha-value>)',
                'on-tertiary-fixed': 'rgb(var(--on-tertiary-fixed) / <alpha-value>)',
                'tertiary-fixed-dim': 'rgb(var(--tertiary-fixed-dim) / <alpha-value>)',
                'on-tertiary-fixed-variant': 'rgb(var(--on-tertiary-fixed-variant) / <alpha-value>)',
                'surface-dim': 'rgb(var(--surface-dim) / <alpha-value>)',
                'surface-bright': 'rgb(var(--surface-bright) / <alpha-value>)',
                'surface-container-lowest': 'rgb(var(--surface-container-lowest) / <alpha-value>)',
                'surface-container-low': 'rgb(var(--surface-container-low) / <alpha-value>)',
                'surface-container': 'rgb(var(--surface-container) / <alpha-value>)',
                'surface-container-high': 'rgb(var(--surface-container-high) / <alpha-value>)',
                'surface-container-highest': 'rgb(var(--surface-container-highest) / <alpha-value>)'
            },

            fontFamily: {
                'afacad': ['"Afacad"', 'serif']
            },
            
            backgroundImage: {
                'gradient-radial': 'radial-gradient(var(--tw-gradient-stops))',
                'gradient-conic':
                'conic-gradient(from 180deg at 50% 50%, var(--tw-gradient-stops))',
            },
            
            margin: {
                '1/2': '50%',
            },
            padding: {
                '13': '3.25rem'
            },
            inset: {
                '13': '3.25rem'
            },
            
            height: {
                'screen-1/2': '50vh',
                'screen-1/3': '33vh',
                'screen-2/3': '66vh',
                'screen-1/4': '25vh',
                'screen-2/4': '50vh',
                'screen-3/4': '75vh',
                'screen-1/5': '20vh',
                'screen-2/5': '40vh',
                'screen-3/5': '60vh',
                'screen-4/5': '80vh',
                'screen-1/6': '16vh',
                'screen-2/6': '33vh',
                'screen-3/6': '50vh',
                'screen-4/6': '66vh',
                'screen-5/6': '83vh',
            },
            minWidth: {
                'xs': '20rem',
                'sm': '24rem',
                'md': '28rem',
                'lg': '32rem',
                'xl': '36rem',
                '2xl': '42rem',
                '3xl': '48rem',
                '4xl': '56rem',
                '5xl': '64rem',
                '6xl': '72rem',
                '7xl': '80rem',
                '8xl': '88rem',
                '9xl': '96rem'
            },
            maxWidth: {
                '8xl': '88rem',
                '9xl': '96rem'
            },
            
            strokeWidth: {
                '3': '3px'
            },
            
            boxShadow: {
                'inner-x': 'inset 8px 0px 10px -10px inset -8px 0px 10px -10px',
                'inner-y': 'inset 0px 8px 10px -10px, inset 0px -8px 10px -10px',
                'inner-t': 'inset 0px 8px 10px -10px',
                'inner-b': 'inset 0px -8px 10px -10px',
                'inner-l': 'inset 8px 0px 10px -10px',
                'inner-r': 'inset -8px 0px 10px -10px',
                
                'hard-md': '0px 5px 12px 5px rgba(0, 0, 0, 0.5)'
            },
            
            screens: {
                'xs': '475px',
                ...defaultTheme.screens
            }
        },
    },
    plugins: [
        function ({ addVariant }) {
            addVariant('child', '& > *');
            addVariant('child-hover', '& > *:hover');
            addVariant('descendant', '& *');
            addVariant('descendant-hover', '& *:hover');
        }
    ]
}

