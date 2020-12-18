import { Pane } from 'evergreen-ui';

const Container = ({ children }) => {
  return (
    <Pane maxWidth={840} marginX="auto" paddingX={20}>
      {children}
    </Pane>
  );
};

export default Container;
